alter table tipo add column tipo_subisidiado boolean default true;
UPDATE tipo set tipo_subisidiado = FALSE WHERE tipo_id = 4;
UPDATE tipo set tipo_subisidiado = FALSE WHERE tipo_id = 5;
UPDATE tipo set tipo_subisidiado = FALSE WHERE tipo_id = 6;
UPDATE tipo set tipo_subisidiado = FALSE WHERE tipo_id = 7;