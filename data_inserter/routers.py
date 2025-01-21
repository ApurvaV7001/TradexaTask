class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'users':
            return 'users'
        elif model._meta.db_table == 'products':
            return 'products'
        elif model._meta.db_table == 'orders':
            return 'orders'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'user' and db == 'users':
            return True
        if model_name == 'product' and db == 'products':
            return True
        if model_name == 'order' and db == 'orders':
            return True
        return False
