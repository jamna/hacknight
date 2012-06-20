# -*- coding: utf-8 -*-

import flask.ext.wtf as wtf
from baseframe.forms import Form, RichTextField, DateTimeField

__all__ = ['EventForm', 'ConfirmWithdrawForm']


class EventForm(Form):
    title = wtf.TextField("Title", description="Name of the Event", validators=[wtf.Required(), wtf.NoneOf(values=["New"])])
    description = RichTextField("Description", description="Description of the project")
    venue_id = wtf.SelectField("Venue", description="Select the venue, don't forget to create a one in venue/new", coerce=int, validators=[wtf.Required()])
    start_datetime = DateTimeField("Start Date and Time", description="Hacknight Start DateTime", validators=[wtf.Required()])
    end_datetime = DateTimeField("End Date and Time", description="Hacknight End DateTime", validators=[wtf.Required()])
    ticket_price = wtf.TextField("Ticket Price", description="Entry fee, if any, to be paid at the venue.")
    total_participants = wtf.IntegerField("Total Participants", description="Total Participants for Hacknight. E.g: 50", default=50, validators=[wtf.Required()])
    website = wtf.TextField("Website", description="Related Website (Optional)", validators=[wtf.Optional()])

    def validate_end_datetime(self, field):
        if field.data < self.start_datetime.data:
            raise wtf.ValidationError(u"Your event can’t end before it starts.")


class ConfirmWithdrawForm(wtf.Form):
    """
    Confirm a delete operation
    """
    delete = wtf.SubmitField(u"Withdraw")
    cancel = wtf.SubmitField(u"Cancel")
