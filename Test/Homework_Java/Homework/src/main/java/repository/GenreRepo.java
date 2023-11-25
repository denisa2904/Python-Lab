package repository;

import entity.Genre;

import java.util.List;
import java.util.Optional;

public class GenreRepo extends AbstractRepository<Genre, Integer> {

    public GenreRepo() {
        super();
    }

    @Override
    public Optional<Genre> findById(Integer integer) {
        return em.createQuery("SELECT g FROM Genre g WHERE g.id = :id", Genre.class)
                .setParameter("id", integer)
                .getResultStream()
                .findFirst();
    }

    @Override
    public List<Genre> findAll() {
        return em.createQuery("SELECT g FROM Genre g", Genre.class)
                .getResultList();
    }

    @Override
    public Optional<Genre> findByName(String name) {
        return em.createQuery("SELECT g FROM Genre g WHERE g.name = :name", Genre.class)
                .setParameter("name", name)
                .getResultStream()
                .findFirst();
    }
}
