package entity;

import jakarta.persistence.*;

import java.sql.Date;
import java.util.List;

@Entity
@Table(name = "playlist", schema = "public", catalog = "lab9")
public class Playlist extends AbstractEntity{
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id")
    private int id;
    @Basic
    @Column(name = "created_at")
    private Date createdAt;
    @Basic
    @Column(name = "name")
    private String name;
    @ManyToMany
    @JoinTable(
            name = "playlists_albums_associations",
            joinColumns = @JoinColumn(name = "playlist_id"),
            inverseJoinColumns = @JoinColumn(name = "album_id")
    )
    private List<Album> albums;

    public Playlist() {
    }

    public Playlist(String name, List<Album> albums) {
        setName(name);
        setAlbums(albums);
        this.createdAt = new Date(System.currentTimeMillis());
    }

    public int getId() {
        return id;
    }
    public Date getCreatedAt() {
        return createdAt;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Album> getAlbums() {
        return albums;
    }

    public void setAlbums(List<Album> albums) {
        this.albums = albums;
    }

    @Override
    public String toString() {
        return "Playlist{" +
                "id=" + getId() +
                ", createdAt=" + getCreatedAt() +
                ", name='" + getName() + '\'' +
                ", albums=" + getAlbums() +
                '}';
    }
}
