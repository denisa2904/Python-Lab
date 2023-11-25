package entity;

import jakarta.persistence.*;

import java.util.List;
import java.util.Objects;

@Entity
@Table(name = "albums", schema = "public", catalog = "lab9")
public class Album extends AbstractEntity{
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id")
    private int id;
    @Basic
    @Column(name = "release_year")
    private int releaseYear;
    @Basic
    @Column(name = "name")
    private String name;

    @ManyToOne
    @JoinColumn(name = "artist_id", referencedColumnName = "id")
    private Artist artist;

    @ManyToMany
    @JoinTable(
            name = "albums_genres_associations",
            joinColumns = @JoinColumn(name = "album_id"),
            inverseJoinColumns = @JoinColumn(name = "genre_id")
    )
    private List<Genre> genres;
    @ManyToMany(mappedBy = "albums")
    private List<Playlist> playlists;

    public Album() {
    }

    public Album(int releaseYear, String name, Artist artist, List<Genre> genres) {
        setReleaseYear(releaseYear);
        setName(name);
        setArtist(artist);
        setGenres(genres);
    }

    public int getId() {
        return id;
    }
    public int getReleaseYear() {
        return releaseYear;
    }

    public void setReleaseYear(int releaseYear) {
        this.releaseYear = releaseYear;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Artist getArtist() {
        return artist;
    }

    public void setArtist(Artist artist) {
        this.artist = artist;
    }

    public List<Genre> getGenres() {
        return genres;
    }

    public void setGenres(List<Genre> genres) {
        this.genres = genres;
    }

    @Override
    public String toString() {
        return "Album{" +
                "id=" + getId() +
                ", releaseYear=" + getReleaseYear() +
                ", name='" + getName() + '\'' +
                ", artist=" + getArtist() +
                ", genres=" + getGenres() +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Album album = (Album) o;

        if (id != album.id) return false;
        if (releaseYear != album.releaseYear) return false;
        if (!Objects.equals(name, album.name)) return false;
        if (!Objects.equals(artist, album.artist)) return false;
        return Objects.equals(genres, album.genres);
    }

    @Override
    public int hashCode() {
        int result = id;
        result = 31 * result + releaseYear;
        result = 31 * result + (name != null ? name.hashCode() : 0);
        result = 31 * result + (artist != null ? artist.hashCode() : 0);
        result = 31 * result + (genres != null ? genres.hashCode() : 0);
        return result;
    }
}
