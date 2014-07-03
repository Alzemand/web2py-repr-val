db.define_table('tb_teste'
               , Field('CCPF', 'decimal(11,0)')
               , Field('CCNPJ', 'decimal(14,0)')
               , Field('SALARIO', 'decimal(8,2)')
               , Field('CBARRA1', 'decimal(12,0)'))

tb_teste                   = db['tb_teste']

tb_teste.id.writable       = False
tb_teste.CCPF.label        = 'CPF'
tb_teste.CCPF.writable     = True
tb_teste.CCPF.requires     = [IS_NOT_EMPTY(), IS_CPF()]
tb_teste.CCPF.represent    = lambda value, row: MASK_CPF()(value)
tb_teste.CCNPJ.label       = 'CNPJ'
tb_teste.CCNPJ.writable    = True
tb_teste.CCNPJ.requires    = [IS_NOT_EMPTY(), IS_CNPJ()]
tb_teste.CCNPJ.represent   = lambda value, row: MASK_CNPJ()(value)
tb_teste.SALARIO.label     = 'Salário'
tb_teste.SALARIO.writable  = True
tb_teste.SALARIO.requires  = [IS_NOT_EMPTY(), IS_MONEY(0 ,999999.99, , dot=',', symbol='€')]
tb_teste.SALARIO.represent = lambda value, row: MASK_MONEY(dot=',', symbol='€')(value, 2)
tb_teste.CBARRA1.label     = 'Codigo de Barras'
tb_teste.CBARRA1.writable  = True
tb_teste.CBARRA1.requires  = [IS_NOT_EMPTY(), IS_MODULO_10()]
tb_teste.CBARRA1.represent = lambda value, row: MASK_DV('-')(value)