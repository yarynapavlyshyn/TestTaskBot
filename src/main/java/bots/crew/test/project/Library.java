package bots.crew.test.project;

import bots.crew.test.project.Imp.ILibrary;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Library implements ILibrary {
    public static List<Book> books = new ArrayList();

    public static void main(String args[]) throws Exception {
        Library library = new Library();
        Scanner scan = new Scanner(System.in);

        while (true) {
            String input = scan.nextLine();
            Request request = new Request(input);
            library.performRequest(request);
        }
    }

    private void performRequest (Request request) throws Exception {
        switch(request.action){
            case ADD:
                addBook(request.author, request.bookName);
                break;
            case REMOVE:
                removeBook(request.bookName);
                break;
            case SHOWaLL:
                printOutAllBooks();
                break;
            case EDIT:
                editBook(request.bookName, request.newBookName);
                break;
        }
    }

    public void addBook(String author, String bookName){
        Book book = new Book(author, bookName);
        books.add(book);
        System.out.println("The book " + book.toString() + " was added.");
    }

    public void editBook(String bookName, String newBookName) throws Exception {
        List<Book> foundBooks = findBooks(bookName);

        Book book = verifyBookToWorkWith(foundBooks, "We have " +
                "few books with such name please choose one by typing a number of book:");
        book.setBookName(newBookName);
        System.out.println("The book " + book.toString() + " was edited: name was changed from " + bookName);
    }
    
    public void removeBook(String bookName) throws Exception {
        List<Book> foundBooks = findBooks(bookName);

        Book book = verifyBookToWorkWith(foundBooks, "We have " +
                "few books with such name please choose one by typing a number of book:");
        books.remove(book);
        System.out.println("The book " + book.toString() + " was removed.");
    }

    private Book verifyBookToWorkWith(List<Book> foundBooks, String
            messageInCaseOfMultipleChoices) throws Exception {
        // if there is only one book with such a name we just choose this one to work with
        if (foundBooks.size() == 1){
            Book theLonelyCandidate = foundBooks.get(0);
            return theLonelyCandidate;
        }
        // if there is not such a book - user made a mistake perhaps
        if (foundBooks.size() == 0) {
            throw new Exception("There is no such a book, sorry. Try another name.");
        }
        // if some books - user is supposed to make a choice
        Book chosenBook = userChooseBookFromList(messageInCaseOfMultipleChoices, foundBooks);
            return chosenBook;
    }

    private Book userChooseBookFromList(String message, List<Book> _books){
        Scanner scan = new Scanner(System.in);

        System.out.println(message);
        int n = 1;
        for (Book book: _books){
            System.out.println(n + ". " + book.toString());
        }
        int chosenBookNum = scan.nextInt();
        return _books.get(n-1);
    }

    private List<Book> findBooks(String bookName){
        List<Book> foundBooks = new ArrayList();
        int i = 0;
        for (Book book: books){
            if (book.getBookName().equals(bookName)){
                foundBooks.add(book);
            }
            i++;
        }
        return foundBooks;
    }

    public void printOutAllBooks(){
        System.out.println("Our books:");

        for (Book book: books) {
            System.out.println("    " + book.toString());
        }
    }
}
