package bots.crew.test.project.Imp;

public interface ILibrary{
    void addBook(String author, String bookname);
    void editBook(String bookName, String newBookName) throws Exception;
    void removeBook(String bookName) throws Exception;
    void printOutAllBooks();
}
