import credmark.model


@credmark.model(slug='pi',
                version='1.0',
                display_name='PI',
                description='PI')
class PIModel:
    context: credmark.model.ModelContext

    def run(self, input) -> dict:
        return {'value': 3.1415}
