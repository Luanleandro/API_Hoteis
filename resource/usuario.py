from models.usuario import UserModel
from flask_jwt_extended import create_access_token,jwt_required, get_jwt
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp 
from blacklist import BLACKLIST

atributos = reqparse.RequestParser()
atributos.add_argument('login', type = str, required = True, help = "The field 'login' cannot be left blank")      
atributos.add_argument('senha', type = str, required = True, help = "The field 'senha' be left blank")  

class User(Resource):
   
   #/usuarios/{user_id}
    def get(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            return user.json()
        return{'Message': 'user not found'}, 404 # not found    

    @jwt_required()
    def delete(self, user_id):
        user = UserModel.find_user(user_id)
        if user:
            user.delete_user()
            return {'message': 'user deleted.'}
        return {'message': 'user not found'}, 404     

class UserRegister(Resource):


    def post(self):
        dados = atributos.parse_args()

        if UserModel.find_by_login(dados['login']):
            return {'message': f"the login '{dados['login']}' alredy exists."} 

        user = UserModel(**dados)
        try:
            user.save_user()
        except:
            return {'message': 'an internal error ocurred trying to save user'}, 500    
        return {'message': "user created sucessfully!!"}, 201

class UserLogin(Resource):

    @classmethod
    def post(cls):

        dados = atributos.parse_args()
        
        user = UserModel.find_by_login(dados['login'])

        if user and safe_str_cmp(user.senha, dados['senha']):
            token_de_acesso = create_access_token(identity=user.user_id)
            return {'acess token': token_de_acesso}, 200
        return {'acess_token': 'The username or password is incorrect'}, 401

class UserLogout(Resource):

    @jwt_required()
    def post(self):
        jwt_id = get_jwt()['jti'] # JWT Token Identifier   
        BLACKLIST.add(jwt_id)
        return   {'message': 'Logout successfully!'}, 200     
