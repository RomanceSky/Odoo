# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
   
    def _default_session(self):
#        return self.env['openacademy.session'].browse(self._context.get('active_id'))
         return self.env['openacademy.session'].browse(self._context.get('active_id'))
    session_id = fields.Many2one('openacademy.session',
        string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.muti
    def subscribe(self):
        for session in self.session_ids:
            self.session_id.attendee_ids |= self.attendee_ids
	return {}
