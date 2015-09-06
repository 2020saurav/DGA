import src.util.logger as logger

log = logger.getLogger("Log Test")

try:
    a = 1/0
except:
    log.error("Div by 0", exc_info=True)

log.info("Info log test")
log.debug("Debug log test")
