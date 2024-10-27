CREATE TABLE estabelecimento (
   	nipcc bigint PRIMARY KEY,
	denominacao VARCHAR(255),
	sede_cep NUMERIC,
	sede_endereco VARCHAR(255),
	cep_intervencao NUMERIC,
	end_intervencao VARCHAR(255),
	email VARCHAR(255),
	senha VARCHAR(255),
	confirmacao_senha VARCHAR(255),
	cid_id bigint,
	dst_id bigint,
	atv_id bigint,
	obj_id bigint,
	CONSTRAINT fk_cid_id
      FOREIGN KEY(cid_id)
        REFERENCES cidade(cid_id),
	CONSTRAINT fk_dst_id
      FOREIGN KEY(dst_id)
        REFERENCES distrito(dst_id),
	CONSTRAINT fk_atv_id
      FOREIGN KEY(atv_id)
        REFERENCES atividade(atv_id),
	CONSTRAINT fk_obj_id
      FOREIGN KEY(obj_id)
        REFERENCES objeto(obj_id)
);

CREATE TABLE atividade (
   	atv_id bigint PRIMARY KEY,
	atv_descricao VARCHAR(255)
);


CREATE TABLE objeto (
   	obj_id bigint PRIMARY KEY,
	obj_descricao VARCHAR(255)
);


CREATE TABLE distrito (
   	dst_id bigint PRIMARY KEY,
	dst_descricao VARCHAR(255)
);

CREATE TABLE cidade (
   	cid_id bigint PRIMARY KEY,
	cid_descricao VARCHAR(255)
);

CREATE TABLE equipamento (
   	eqp_id bigint PRIMARY KEY,
	eqp_descricao VARCHAR(255)
);