import esphome.codegen as cg
from esphome import automation
from esphome.const import CONF_ID

tft_ns = cg.global_ns.namespace('')  # Global namespace
TFTeSPIComponent = tft_ns.class_('tft_espi_lvgl', cg.Component)

CONFIG_SCHEMA = cg.Schema({
    cg.GenerateID(): cg.declare_id(TFTeSPIComponent),
}).extend(cg.COMPONENT_SCHEMA)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)