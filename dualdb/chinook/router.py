class ChinookRouter(object): 

    APP_LABEL = 'chinook'
    # These two are the one defined in DATABASES settings
    CHINOOK_DB = 'chinookdb'
    DEFAULT = 'default'

    def db_for_read(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == self.APP_LABEL:
            return self.CHINOOK_DB
        return self.DEFAULT

    def db_for_write(self, model, **hints):
        "Point all operations on chinook models to 'chinookdb'"
        if model._meta.app_label == self.APP_LABEL:
            return self.CHINOOK_DB
        return self.DEFAULT
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in chinook app"
        if obj1._meta.app_label == self.APP_LABEL and obj2._meta.app_label == self.APP_LABEL:
            return True
        # Allow if neither is chinook app
        elif self.APP_LABEL not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return True
        return False
    
    def allow_syncdb(self, db, model):
        if db == self.CHINOOK_DB or model._meta.app_label == self.APP_LABEL:
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True
