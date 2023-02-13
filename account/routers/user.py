from fastapi import APIRouter, Depends
from bson.objectid import ObjectId
from account.serializers.user import userResponseEntity

from account.database import User
from .. import schemas, oauth2

router = APIRouter()

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user),):
    try:
        user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
        return {"status": "success", "user": user}
    except:
        return {"error": schemas}
        

