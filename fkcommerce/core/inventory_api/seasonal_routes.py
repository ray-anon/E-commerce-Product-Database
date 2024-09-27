from apifairy import response , body

from core.inventory_api import inventory_seasonal_api_blueprint

from core.schema import SeasonalSchema 

from core.models import SeasonalEvent

from core import database

seasonal_schema = SeasonalSchema()



@inventory_seasonal_api_blueprint.route("/seasonal" , methods=['POST'])
@body(seasonal_schema)
@response(seasonal_schema)
def seasonal_insert(kwargs):
    print(kwargs)
    new_seasonal = SeasonalEvent(**kwargs)
    database.session.add(new_seasonal)
    database.session.commit()
    return new_seasonal