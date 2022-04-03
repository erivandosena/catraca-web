
CREATE TABLE vaccine_declaration (
        id serial NOT NULL, 
        CONSTRAINT pk_vaccine_declaration PRIMARY KEY (id), 
        id_user_sig integer, 
        dose_number integer, 
        card_file character varying(200), 
        status character varying(400), 
        created_at timestamp without time zone
);
