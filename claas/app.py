import os
from flakon import create_app
from claas.views import base_scenario, skeleton_v1, fashion_scenario

app = create_app(blueprints=[base_scenario, skeleton_v1, fashion_scenario])
