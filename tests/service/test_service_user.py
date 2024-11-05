from src.service.service_user import ServiceUser

class TestServiceUser:

    def test_add_success(self):
        name_add = 'Thiago'
        job_add = 'TechLead'
        result_expect = 'Usuario adicionado com sucesso'
        service = ServiceUser()

        result = service.add_user(name=name_add, job=job_add)

        assert result_expect == result

    def test_add_user_invalid(SELF):
        name_add_invalid = 456
        job_add = 'TI'
        resultado_esperado = 'Nome ou Profissão precisa ser um texto'

        service = ServiceUser()

        resultado = service.add_user(name=name_add_invalid, job=job_add)

        assert resultado_esperado == resultado

    def test_add_user_not_found(SELF):
        name_add_invalid = None
        job_add = 'TI'
        resultado_esperado = 'Usuario nao adicionado'

        service = ServiceUser()

        resultado = service.add_user(name=name_add_invalid, job=job_add)

        assert resultado_esperado == resultado

    def test_validate_null_job(self):
        name_null = 'Matheus'
        job_null = None
        result_expect = 'Usuario nao adicionado'
        service = ServiceUser()

        result = service.add_user(name=name_null, job=job_null)

        assert result_expect == result

    def test_del_name(self):
        user_remove = 'Lucas'
        result_expect = 'Usuario removido'
        service = ServiceUser()

        result = service.del_user(name=user_remove)

        assert result_expect == result

    def test_del_name_not_found(self):
        user_bd = 'Matias'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.del_user(name=user_bd)

        assert result_expect == result

    def test_update_job(self):
        name_user = 'Lucas'
        update_job = 'Master System'
        result_expect = 'Profissão atualizada com sucesso'
        service = ServiceUser()

        result = service.update_user(name=name_user,new_job=update_job)

        assert result_expect == result

    def test_update_job_user_not_found(self):
        name_user = 'Thiago'
        update_job = 'Master System'
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.update_user(name=name_user,new_job=update_job)

        assert result_expect == result

    def test_select_user(self):
        name_user = 'Lucas'
        job = 'Xuxu'
        result_expect = 'Profissão: ' + job
        service = ServiceUser()

        result = service.select_user(name=name_user)

        assert result_expect == result

    def test_select_user_not_found(self):
        name_user = None
        result_expect = 'Usuario não encontrado'
        service = ServiceUser()

        result = service.select_user(name=name_user)

        assert result_expect == result
    