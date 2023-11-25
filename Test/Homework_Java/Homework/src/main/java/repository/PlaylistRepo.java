package repository;

import entity.Playlist;

import java.util.List;
import java.util.Optional;

public class PlaylistRepo extends AbstractRepository<Playlist, Integer> {

    public PlaylistRepo() {
        super();
    }

    @Override
    public Optional<Playlist> findById(Integer integer) {
        return em.createQuery("SELECT p FROM Playlist p WHERE p.id = :id", Playlist.class)
                .setParameter("id", integer)
                .getResultStream()
                .findFirst();
    }

    @Override
    public List<Playlist> findAll() {
        return em.createQuery("SELECT p FROM Playlist p", Playlist.class)
                .getResultList();
    }

    @Override
    public Optional<Playlist> findByName(String name) {
        return em.createQuery("SELECT p FROM Playlist p WHERE p.name = :name", Playlist.class)
                .setParameter("name", name)
                .getResultStream()
                .findFirst();
    }
}
