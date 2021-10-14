from application_services.BaseApplicationResource import BaseApplicationResource
import database_services.RDBService as d_service


class BreederResource(BaseApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_by_template(cls, template):
        res = d_service.find_by_template("searchbase", "breeder",
                                       template, None)
        return res

    @classmethod
    def get_breeder_rating(cls, breederid):
        res = d_service.get_specifc_column("searchbase", "breeder",
                                      "rating", 'id', breederid)
        return res
