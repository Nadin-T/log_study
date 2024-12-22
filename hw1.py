import logging

logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Установка уровня логирования

# Создаем обработчики файлов
debug_info_handler = logging.FileHandler('debug_info.log', encoding='utf-8')
warning_error_handler = logging.FileHandler('warnings_errors.log', encoding='utf-8')

# Установим уровень логирования для каждого обработчика
debug_info_handler.setLevel(logging.DEBUG)  # DEBUG и INFO
warning_error_handler.setLevel(logging.WARNING)  # WARNING и выше

# Настраиваем формат сообщений
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Применяем формат к обработчикам
debug_info_handler.setFormatter(formatter)
warning_error_handler.setFormatter(formatter)

# Добавляем обработчики к логгеру
logger.addHandler(debug_info_handler)
logger.addHandler(warning_error_handler)

# Примеры логирования различных уровней
logger.debug('Это сообщение DEBUG')
logger.info('Это сообщение INFO')
logger.warning('Это сообщение WARNING')
logger.error('Это сообщение ERROR')
logger.critical('Это сообщение CRITICAL')
