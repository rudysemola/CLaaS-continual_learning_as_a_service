import os
from flakon import create_app
from claas.views import scenario_v1, skeleton_v1

app = create_app(blueprints=[scenario_v1, skeleton_v1], host="0.0.0.0", port="5001")


#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port="5001", debug=True)
