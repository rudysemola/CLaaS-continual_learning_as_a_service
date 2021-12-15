import os
from flakon import create_app
from claas.views import scenario_v1, skeleton_v1

app = create_app(blueprints=[scenario_v1, skeleton_v1])
