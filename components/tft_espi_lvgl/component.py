import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID


tft_ns = cg.global_ns.namespace('tft_espi_lvgl')
TFTeSPIComponent = tft_ns.class_('TFTeSPIComponent', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(TFTeSPIComponent),
}).extend(cv.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
