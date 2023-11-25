package repository;

import entity.AbstractEntity;
import jakarta.persistence.EntityManager;

import java.io.Serializable;
import java.util.List;
import java.util.Optional;

public abstract class AbstractRepository<T extends AbstractEntity, ID extends Serializable> {
    protected EntityManager em;

    public AbstractRepository() {
        this.em = DatabaseConnection.getEm();
    }

    public abstract Optional<T> findById(ID id);
    public void create(T entity){
        em.getTransaction().begin();
        em.persist(entity);
        em.getTransaction().commit();
    }
    public abstract List<T> findAll();
    public abstract Optional<T> findByName(String name);
}
