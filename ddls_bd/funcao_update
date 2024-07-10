CREATE OR REPLACE FUNCTION update_medico_percentual(novo_percentual NUMERIC, 
													especialidade_nome TEXT) RETURNS VOID AS $$
BEGIN
    UPDATE MEDICO
    SET Percentual = novo_percentual
    FROM EXERCE_ESPECIALIDADE
    JOIN ESPECIALIDADE ON EXERCE_ESPECIALIDADE.IdEsp = ESPECIALIDADE.IdEsp
    WHERE MEDICO.CRM = EXERCE_ESPECIALIDADE.CRM
    AND ESPECIALIDADE.NomeE = especialidade_nome;
END;
$$ LANGUAGE plpgsql;

SELECT update_medico_percentual(30, 'Cardiologia');
