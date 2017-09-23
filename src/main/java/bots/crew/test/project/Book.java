package bots.crew.test.project;

import bots.crew.test.project.Imp.IBook;

public class Book implements IBook {
    public String author;
    public String bookName;

    public Book(String _author, String _bookName){
        author = _author;
        bookName = _bookName;

    }

    public String getAuthor() {
        return author;
    }

    public String getBookName() {
        return bookName;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public void setBookName(String bookName) {
        this.bookName = bookName;
    }

    @Override
    public boolean equals(Object o) {
        if (o.getClass() != Book.class){
            return false;
        }
        Book boo = (Book) o;
        return this.getAuthor().equals(boo.getAuthor()) &&
                this.getBookName().equals(boo.getBookName());
    }

    @Override
    public String toString() {
        return author + " " + bookName;
    }
}
