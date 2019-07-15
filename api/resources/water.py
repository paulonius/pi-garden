from flask_restful import Resource


class WaterCollection(Resource):
    def get(self):
        """ All or most of the rows """
        pass

    def post(self):
        """ Create new row """
        pass


class Water(Resource):
    def get(self, id):
        """ Get specific water """
        pass

    def put(self, id):
        """ Modify water """
        pass

    def delete(self, id):
        """ Delete water """
        pass
