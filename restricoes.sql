---RESTRICOES

CREATE OR REPLACE FUNCTION verifica_horario_disponivel() 
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM CONSULTA
        WHERE CRM = NEW.CRM
        AND Data = NEW.Data
        AND (
            (HoraInicCon <= NEW.HoraInicCon AND HoraFimCon > NEW.HoraInicCon) OR
            (HoraInicCon < NEW.HoraFimCon AND HoraFimCon >= NEW.HoraFimCon) OR
            (HoraInicCon >= NEW.HoraInicCon AND HoraFimCon <= NEW.HoraFimCon)
        )
    ) THEN
        RAISE EXCEPTION 'Médico já tem uma consulta marcada nesse horário.';
    END IF;

    IF EXISTS (
        SELECT 1 FROM CONSULTA
        WHERE IdPac = NEW.IdPac
        AND Data = NEW.Data
        AND (
            (HoraInicCon <= NEW.HoraInicCon AND HoraFimCon > NEW.HoraInicCon) OR
            (HoraInicCon < NEW.HoraFimCon AND HoraFimCon >= NEW.HoraFimCon) OR
            (HoraInicCon >= NEW.HoraInicCon AND HoraFimCon <= NEW.HoraFimCon)
        )
    ) THEN
        RAISE EXCEPTION 'Paciente já tem uma consulta marcada nesse horário.';
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER verifica_horario_trigger
BEFORE INSERT OR UPDATE ON CONSULTA
FOR EACH ROW EXECUTE FUNCTION verifica_horario_disponivel();



