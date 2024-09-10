Тот пример, который был в задании - знакомо. Давно, в рамках какого то учебного курса, скорее всего на Курсере - делал задачу - найти среднее за один проход по списку. Так как сам код был коротким и простым - никак эти "кусочки" не выделял.

Примеры из более актуальных задач пытался найти - но с этим сложно. На python если и делаю обработку списков - обычно они достаточно короткие, так что не проблема при необходимости на втором этапе прогнать список ещё раз.
На SQL бываю реально огромные таблицы, но это декларативный язык и циклов там нет (если не касаться встроенных процедур)

Наиболее похожее на это - в дагах airflow, которые сами являются генераторами других дагов, иногда возникают ситуации, что параметры читаются в одном месте, а применяются сильно дальше, часто в другом таске или даге. Или, как вариант, параметры приходят из разных источников, но применяются вместе. Как то отдельно эти моменты отправки/обработки параметров обычно не выделяются. Плюс часто бывают ситуации, когда такой генератор дагов под конкретную задачу надо слегка модернизировать, добавляются новые параметры - и получаются такие довольно тяжеловесные конструкции:

```python
  if kwargs['params'].get('is_sql_template', False):
      sql =kwargs['templates_dict']['query']
      logging.info(sql)
  elif 'query_path' in kwargs['params']:
      sql = open(kwargs['params']['query_path'], 'r').read()
  else:
      sql = kwargs['templates_dict'].get('max_cpm_candidates_fill')
      if sql is None:
          raise ValueError('No sql query to execute')
```

С комментариями становится прозрачней

```python
  if 'query_path' in kwargs['params']:  # the path to the file is specified
      sql = open(kwargs['params']['query_path'], 'r').read()
  elif kwargs['params'].get('is_sql_template', False):  # a template is used
      sql =kwargs['templates_dict']['query']
  else:  # a special script is used
      sql = kwargs['templates_dict'].get('max_cpm_candidates_fill')
      if sql is None:
          raise ValueError('No sql query to execute')
  logging.info(sql)
```
