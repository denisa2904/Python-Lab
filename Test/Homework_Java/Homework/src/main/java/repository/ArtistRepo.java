package repository;

import entity.Artist;

import java.util.List;
import java.util.Optional;

public class ArtistRepo extends AbstractRepository<Artist, Integer> {

    public ArtistRepo() {
        super();
    }

    @Override
    public Optional<Artist> findById(Integer integer) {
        return em.createQuery("SELECT a FROM Artist a WHERE a.id = :id", Artist.class)
                .setParameter("id", integer)
                .getResultStream()
                .findFirst();
    }

    @Override
    public List<Artist> findAll() {
        return em.createQuery("SELECT a FROM Artist a", Artist.class)
                .getResultList();
    }

    @Override
    public Optional<Artist> findByName(String name) {
        return em.createQuery("SELECT a FROM Artist a WHERE a.name = :name", Artist.class)
                .setParameter("name", name)
                .getResultStream()
                .findFirst();
    }
}
