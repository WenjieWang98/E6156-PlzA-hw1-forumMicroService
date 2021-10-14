from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class CatResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_breeder_id(cls, catid):
        res = d_service.get_specifc_column("searchbase", "catInfo",
                                      "breeder", 'id', catid)
        return res
        
    @classmethod
    def get_by_template(cls, template):
        res = d_service.find_by_template("searchbase", "catInfo",
                                       template, None)
        return res