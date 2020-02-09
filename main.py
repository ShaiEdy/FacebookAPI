import requests

class PetStoreActions:

    def __init__(self):
        pass

    def createUser(self, userData):
        res = requests.post('https://petstore.swagger.io/v2/user', None, userData)
        #print res.text
        return res

    def getUserByName(self, username):
        res = requests.get('https://petstore.swagger.io/v2/user/%s' % username)
        print res.text
        return res

    def deleteUserByName(self, username):
        res = requests.delete('https://petstore.swagger.io/v2/user/%s' % username)
        print res.text
        return res


if __name__ == '__main__':

    userData = {"id": 0, "username": "shai", "firstName": "Shai", "lastName": "Edy", "email": "shai@gmail.com",
            "password": "12345", "phone": "050-123-4567", "userStatus": 0, 'key': 'value'}

    storeActions = PetStoreActions()

    storeActions.createUser(userData)
    storeActions.getUserByName("shai")
    storeActions.deleteUserByName("shai")
