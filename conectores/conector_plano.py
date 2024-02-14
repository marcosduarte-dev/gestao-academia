from classes.plano import TipoPlano
from database.run_sql import run_sql

def get_all():
  sql = "SELECT * FROM webuser.TB_PLANOS"
  results = run_sql(sql)

  tipo_planos = []

  for result in results:
    tipo_plano = TipoPlano(result['plano'], result['id'])
    tipo_planos.append(tipo_plano)

  return tipo_planos

def get_one(id):
  sql = "SELECT * FROM webuser.TB_PLANOS WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]

  if result is not None:
    tipo_plano = TipoPlano(result['plano'], result['id'])

  return tipo_plano

def new(tipo_plano):
  sql = "INSERT INTO webuser.TB_PLANOS (plano) VALUES (%s) RETURNING *;"
  values = [tipo_plano.plano]
  results = run_sql(sql, values)
  id = results[0]['id']
  tipo_plano.id = id
  return tipo_plano

def delete_one(id):
  sql = "DELETE FROM webuser.TB_PLANOS WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def edit(tipo_plano):
  sql = "UPDATE webuser.TB_PLANOS SET plano = %s WHERE id = %s"
  values = [tipo_plano.plano, tipo_plano.id]
  run_sql(sql, values)