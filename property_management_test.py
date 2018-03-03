"""
Module for property management program testing
"""
import property_management
agent = property_management.Agent()
while True:
    agent.add_property()
    agent.display_properties()
    agent.display_by_payment_types()
    agent.display_by_property_types()
