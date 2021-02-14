#!/usr/bin/env python3
import megacosm

megacosm.app.config.from_object('config.TestConfiguration')


megacosm.app.run(host='0.0.0.0', port=8000, debug=True)
