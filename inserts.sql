INSERT INTO MEDICO (CRM, Nome, Telefone, Percentual) VALUES
('00001', 'Dr. House', '1111-2222', 20.5),
('00002', 'Dr. Kildare', '2222-3333', 18.0),
('00003', 'Dr. Wilson', '3333-4444', 22.1),
('00004', 'Dr. Strange', '4444-5555', 15.0),
('00005', 'Dr. Quinn', '5555-6666', 25.0),
('00006', 'Dr. Omni', '9999-8888', 22.0);

INSERT INTO PACIENTE (IdPac, CPF, NomeP, TelefonePac, Endereco, Idade, Sexo) VALUES
(1, '123.456.789-00', 'Diego Pituca', '6666-7777', 'Rua das Flores, 123', 30, 'M'),
(2, '234.567.890-11', 'Maria Silva', '7777-8888', 'Av. do Sol, 234', 25, 'F'),
(3, '345.678.901-22', 'João Barros', '8888-9999', 'Alameda das Árvores, 345', 45, 'M'),
(4, '456.789.012-33', 'Clara Nunes', '9999-0000', 'Praça Central, 456', 38, 'F'),
(5, '567.890.123-44', 'Lucas Martins', '0000-1111', 'Rua do Comércio, 567', 29, 'M');


INSERT INTO AGENDA (IdAgenda, DiaSemana, HoraInicio, HoraFim, CRM) VALUES
(11, 'Segunda', '08:00', '12:00', '00001'),
(12, 'Terça', '08:00', '12:00', '00001'),
(13, 'Quarta', '08:00', '12:00', '00001'),
(14, 'Quinta', '08:00', '12:00', '00001'),
(15, 'Sexta', '08:00', '12:00', '00001'),
(16, 'Sábado', '08:00', '12:00', '00001'),
(17, 'Domingo', '08:00', '12:00', '00001');

INSERT INTO ESPECIALIDADE (IdEsp, NomeE, Indice) VALUES
(1, 'Cardiologia', 1),
(2, 'Dermatologia', 2),
(3, 'Pediatria', 3),
(4, 'Neurologia', 4),
(5, 'Gastroenterologia', 5);

INSERT INTO EXERCE_ESPECIALIDADE (CRM, IdEsp) VALUES
('00001', 1),  
('00001', 2), 
('00002', 2), 
('00003', 3), 
('00004', 4), 
('00005', 5),
('00006', 1),
('00006', 2),
('00006', 3),
('00006', 4),
('00006', 5);


INSERT INTO CONSULTA (IdCon, CRM, IdEsp, IdPac, Data, HoraInicCon, HoraFimCon, Pagou, ValorPago, FormaPagamento) VALUES
(1, '00001', 1, 1, '2024-01-05', '09:00', '10:00', 1, 300.00, 'Dinheiro'),  -- Dr. House, Cardiologia com Diego Pituca
(2, '00001', 2, 2, '2024-05-10', '10:00', '11:00', 0, 250.00, 'Cartão'),   -- Dr. House, Dermatologia com Maria Silva
(3, '00002', 2, 3, '2024-01-06', '08:00', '09:00', 1, 200.00, 'Cartão'),   -- Dr. Kildare, Dermatologia com João Barros
(4, '00003', 3, 4, '2024-01-07', '14:30', '15:30', 1, 350.00, 'Cheque'),   -- Dr. Wilson, Pediatria com Clara Nunes
(5, '00004', 4, 5, '2024-01-08', '16:00', '17:00', 1, 400.00, 'Dinheiro'), -- Dr. Strange, Neurologia com Lucas Martins
(6, '00001', 1, 3, '2024-02-15', '10:00', '11:00', 0, 280.00, 'Cartão'),   -- Dr. House, Cardiologia com João Barros
(7, '00002', 2, 4, '2024-03-16', '09:30', '10:30', 1, 260.00, 'Dinheiro'), -- Dr. Kildare, Dermatologia com Clara Nunes
(8, '00003', 3, 5, '2024-04-17', '11:00', '12:00', 1, 220.00, 'Cheque'),   -- Dr. Wilson, Pediatria com Lucas Martins
(9, '00005', 5, 1, '2024-05-18', '14:00', '15:00', 1, 300.00, 'Dinheiro'), -- Dr. Quinn, Gastroenterologia com Diego Pituca
(10, '00004', 4, 2, '2024-06-19', '15:30', '16:30', 1, 310.00, 'Cartão'),
(11, '00001', 2, (SELECT IdPac FROM PACIENTE WHERE NomeP = 'Diego Pituca'), '2024-05-10', '10:00', '11:00', 0, 250.00, 'Cartão');

INSERT INTO DIAGNOSTICO (IdDiagnostico, TratamentoRecomendado, RemediosReceitados, Observacoes, IdCon) VALUES
(1, 'Revisão da medicação', 'Atenolol', 'Checar pressão diariamente', 1),
(2, 'Iniciar tratamento de pele', 'Creme hidratante', 'Aplicar duas vezes ao dia', 2),
(3, 'Ajustar dosagem de insulina', 'Insulina', 'Monitorar níveis de glicose', 3),
(4, 'Início de terapia', 'Antidepressivos', 'Avaliar em 30 dias', 4),
(5, 'Modificação da dieta', 'Suplementos', 'Consultar nutricionista', 5);

INSERT INTO DOENCA (IdDoenca, NomeD) VALUES
(1, 'Hipertensão'),
(2, 'Eczema'),
(3, 'Diabetes'),
(4, 'Depressão'),
(5, 'Deficiência de ferro');
INSERT INTO DIAGNOSTICA (IdDiagnostico, IdDoenca) VALUES
(1, 1),  -- Hipertensão
(2, 2),  -- Eczema
(3, 3),  -- Diabetes
(4, 4),  -- Depressão
(5, 5);  -- Deficiência de ferro

