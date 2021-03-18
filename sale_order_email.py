from odoo import api, fields, models

class SaleOrderEmail(models.Model):
    _inherit = "sale.order"

    def action_send_myemail(self):
        self.ensure_one()
        template_id = self.env.ref('sale_order_email.sale_email_template').id
        temp = self.env['mail.template'].browse(template_id)
        compose_form = self.env.ref('mail.email_compose_message_wizard_form', False)
        ctx = dict(
            default_model='sale.order',
            default_res_id=self.id,
            default_use_template=bool(temp),
            default_template_id=temp and temp.id or False,
            default_composition_mode='comment',
            mark_invoice_as_sent=True,
            # custom_layout="account.mail_template_data_notification_email_account_invoice"
        )
        return {
            'name': 'Compose Email',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(compose_form.id, 'form')],
            'view_id': compose_form.id,
            'target': 'new',
            'context': ctx,
        }


