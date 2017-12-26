CREATE OR REPLACE TRIGGER meeting_insert
  BEFORE INSERT ON "Meeting"
  FOR EACH ROW
  BEGIN
    IF :NEW."date" <= SYSDATE THEN
      RAISE_APPLICATION_ERROR(-20001, 'DATE CAN NOT BE IN PAST');
    END IF;
    SELECT meeting_seq.NEXTVAL
      INTO :NEW."id"
      FROM dual;
  END;
