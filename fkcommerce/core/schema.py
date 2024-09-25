from core import ma

class CategoryResponseSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)

class CategoryInsertSchema(ma.Schema):
    name = ma.String(required=True)
    slug = ma.String(required=True)
    is_active = ma.Boolean(required=True)
    parent_id = ma.Integer(allow_none=True)

class ProductSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    slug = ma.String(required=True)
    description = ma.String()
    is_digital = ma.Boolean(required=True)
    is_active = ma.Boolean(required=True)
    category_id = ma.Integer()
    stock_status = ma.String(dump_only=True)
    created_at = ma.DateTime(dump_only=True)
    
class ProductLineSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    price = ma.Decimal(places=2)
    sku = ma.String(dump_only=True)
    stock_qty = ma.Integer()
    is_active = ma.Boolean(required=True)
    order = ma.Integer()
    weight = ma.Float()
    product_id = ma.Integer()
    created_at = ma.DateTime(dump_only=True)

class ProductLineImageSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    alternative_text = ma.String(max_length=200)
    url = ma.String()
    order = ma.Integer()
    product_line_id = ma.Integer()

class AttributeSchema(ma.Schema):
    id = ma.Integer(dump_only=True)
    name = ma.String(required=True)
    description = ma.String()