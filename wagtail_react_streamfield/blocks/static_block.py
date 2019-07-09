from wagtail.core.blocks import StaticBlock, Block


class NewStaticBlock(StaticBlock):
    def get_definition(self, **kwargs):
        definition = Block.get_definition(self)
        definition.update(
            isStatic=True,
            html=self.render_form(self.get_default(),
                                  prefix=self.FIELD_NAME_TEMPLATE),
        )
        return definition
