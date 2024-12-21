from erpnext.selling.doctype.sales_order.sales_order import SalesOrder

class SalesOrder2(SalesOrder):
    def validate(self):
        # Optional: Add custom validations
        super().validate()