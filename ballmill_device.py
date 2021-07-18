import wiotp.sdk.device
import random
import time


def myCommandCallback(cmd):
    print("Command received: %s" % cmd.data)


# Configure

myConfig = {
    "identity": {
        "orgId": "vrvzh6",
        "typeId": "ballmill",
        "deviceId": "ballmill_device_1"

    },
    "auth": {
        "token": "zUkBbh7uhWbou-E)WL"
    }
}
# myConfig = wiotp.sdk.device.parseConfigFile("device.yaml")
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.commandCallback = myCommandCallback

# Connect
client.connect()

# Send Data
while True:
    myData = {'ball_mill_id': "Mill1", 'plant_id': "opt_Arizona",
              'entity_id': "2dfef741-5ff6-405a-a290-63d66b69735f", 'total_fresh_feed': float(
            "{0:.6f}".format(30.0, 35.0)),
              "seperator_speed": float("{0:.6f}".format(800.0, 1200.0)),
              'a15_1_register_position': float("{0:.6f}".format(800.0, 1200.0)),
              'a10_1_fan_current': float("{0:.6f}".format(3.0, 4.0)), 'a10_2_fan_current': float(
            "{0:.6f}".format(3.0, 5.0)),
              'bucket_elevator_power': float("{0:.6f}".format(20.0, 35.0)), 'liquid_additive': "169",
              'mill_outlet_pressure': float(
                  "{0:.6f}".format(20.0, 35.0)),
              'position_comp_a9': float("{0:.6f}".format(-5.0, 100.0)),
              'rejects_flow_rate': float("{0:.6f}".format(300.0, 500.0)),
              'separator_inlet_pressure': float("{0:.6f}".format(250.0, 300.0)),
              'separator_outlet_temperature': float("{0:.6f}".format(80.0, 90.0)), 'puz_weighfeeder_flow':
                  float("{0:.6f}".format(0.0, 15.0)), 'fly_ash_weighfeeder_flow': "0",
              'limestone_feed_rate': float("{0:.6f}".format(0.0, 20.0)), 'clinker_flow_rate':
                  float("{0:.6f}".format(45.0, 65.0)),
              'seperator_power': float("{0:.6f}".format(25.0, 50.0)),
              'main_motor_power': float("{0:.4f}".format(1900.0, 2100.0)),
              'main_fan_power': float("{0:.6f}".format(30.0, 80.0)),
              'cm1_inlet_millscan': float("{0:.4f}".format(15.0, 100.0)), 'cement_temperature':
                  float("{0:.6f}".format(70.0, 120.0)),
              'gypsum_feed_rate': float("{0:.6f}".format(4.0, 5.0))}
    client.publishEvent(eventId="evt_ballmill_data", msgFormat="json", data=myData, qos=0, onPublish=None)
    time.sleep(5)

# Disconnect
client.disconnect()
