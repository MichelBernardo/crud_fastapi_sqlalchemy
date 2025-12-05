from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.tshirt_model import TShirtModel
from schemas.tshirt_schema import TShirtSchema
from core.deps import get_session


router = APIRouter()


# GET T-shirts
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[TShirtSchema])
async def get_tshirts(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TShirtModel)
        result = await session.execute(query)
        tshirts: List[TShirtModel] = result.scalars().all()

        return tshirts


# GET T-shirt
@router.get('/{tshirt_id}', status_code=status.HTTP_200_OK, response_model=TShirtSchema)
async def get_tshirt(tshirt_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TShirtModel).filter(TShirtModel.id == tshirt_id)
        result = await session.execute(query)
        tshirt: TShirtModel = result.scalar_one_or_none()

        if tshirt:
            return tshirt
        else:
            raise HTTPException(detail='T-shirt not found.', status_code=status.HTTP_404_NOT_FOUND)


# POST T-shirt
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=TShirtSchema)
async def post_tshirt(tshirt: TShirtSchema, db: AsyncSession = Depends(get_session)):
    new_tshirt = TShirtModel(age=tshirt.age, size=tshirt.size, gender=tshirt.gender)

    db.add(new_tshirt)
    await db.commit()

    return new_tshirt


# PUT T-shirt
@router.put('/{tshirt_id}', status_code=status.HTTP_202_ACCEPTED, response_model=TShirtSchema)
async def put_tshirt(tshirt_id: int, tshirt: TShirtSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TShirtModel).filter(TShirtModel.id == tshirt_id)
        result = await session.execute(query)
        tshirt_to_update = result.scalar_one_or_none()

        if tshirt_to_update:
            tshirt_to_update.age = tshirt.age
            tshirt_to_update.size = tshirt.size
            tshirt_to_update.gender = tshirt.gender

            await session.commit()
            return tshirt_to_update
        else:
            raise HTTPException(detail='T-shirt not found.', status_code=status.HTTP_404_NOT_FOUND)


# DELETE T-shirt
@router.delete('/{tshirt_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_tshirt(tshirt_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TShirtModel).filter(TShirtModel.id == tshirt_id)
        result = await session.execute(query)
        tshirt_to_delete = result.scalar_one_or_none()

        if tshirt_to_delete:
            await session.delete(tshirt_to_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='T-shirt not found.', status_code=status.HTTP_404_NOT_FOUND)