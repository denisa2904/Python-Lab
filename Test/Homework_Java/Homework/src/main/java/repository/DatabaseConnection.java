package repository;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;

public class DatabaseConnection {

    private static final EntityManagerFactory emf = Persistence.createEntityManagerFactory("lab9");
    private static final EntityManager em = emf.createEntityManager();

    public static EntityManager getEm() {
        return em;
    }

    private DatabaseConnection() {
    }
}
