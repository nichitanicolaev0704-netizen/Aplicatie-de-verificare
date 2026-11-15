# logic.py

def verifica_dependenta_functionala(date_tabel, nume_coloane, indici_X, indici_Y):
    """
    Verifică dacă X -> Y este respectată.
    Returnează: (True, "") sau (False, mesaj_detaliat_conflict)
    """
    mapa_X_Y = {}

    for idx_rand, rand in enumerate(date_tabel):
        val_X = tuple(rand[i] for i in indici_X)
        val_Y = tuple(rand[i] for i in indici_Y)

        if val_X in mapa_X_Y:
            val_Y_anterioara, rand_anterior = mapa_X_Y[val_X]
            if val_Y_anterioara != val_Y:
                nume_X = [nume_coloane[i] for i in indici_X]
                detalii_conflict = (
                    f"Conflict detectat!\n\n"
                    f"Pentru determinantul X ({', '.join(nume_X)}) = {val_X}:\n"
                    f"- La rândul {rand_anterior + 1}, determinatul Y are valoarea: {val_Y_anterioara}\n"
                    f"- La rândul {idx_rand + 1}, determinatul Y are valoarea diferită: {val_Y}\n\n"
                    f"Regula X -> Y este ÎNCĂLKATĂ!"
                )
                return False, detalii_conflict
        else:
            mapa_X_Y[val_X] = (val_Y, idx_rand)

    return True, "Dependența funcțională este respectată integral!"
