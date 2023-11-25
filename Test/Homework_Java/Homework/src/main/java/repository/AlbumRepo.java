package repository;

import entity.Album;

import java.util.List;
import java.util.Optional;

public class AlbumRepo extends AbstractRepository<Album, Integer> {

    public AlbumRepo() {
        super();
    }

    @Override
    public Optional<Album> findById(Integer integer) {
        return em.createQuery("SELECT a FROM Album a WHERE a.id = :id", Album.class)
                .setParameter("id", integer)
                .getResultStream()
                .findFirst();
    }

    @Override
    public List<Album> findAll() {
        return em.createQuery("SELECT a FROM Album a", Album.class)
                .getResultList();
    }

    @Override
    public Optional<Album> findByName(String name) {
        return em.createQuery("SELECT a FROM Album a WHERE a.name = :name", Album.class)
                .setParameter("name", name)
                .getResultStream()
                .findFirst();
    }
}
