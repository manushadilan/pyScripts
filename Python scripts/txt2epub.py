from ebooklib import epub

def create_epub(book):

    #read text file
    with open('player who returned 10000 years later.txt','r', encoding='utf-8') as file :
        text = file.read()

    chapters =text.split('\n\n\n')
    spine = ['nav']
    toc = []

    for chapter_id, chapter_content_full in enumerate(chapters):

        chapter_lines = chapter_content_full.split("\n\n")
        chapter_title = chapter_lines[0]
        chapter_content = chapter_lines[1:]

        # write chapter title and contents
        chapter = epub.EpubHtml(
                title=chapter_title,
                file_name="chap_{:02d}.xhtml".format(chapter_id + 1),
                lang='en',
        )
        chapter.content = "<h1>{}</h1>{}".format(
                chapter_title,
                "".join("<p>{}</p>".format(line) for line in chapter_content),
        )

        # add chapter to the book and TOC
        book.add_item(chapter)
        spine.append(chapter)
        toc.append(chapter)
    
    # update book spine and TOC
    book.spine = spine
    book.toc = toc

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    output_file = 'player who returned 10000 years later.epub' #.with_suffix(".epub")

    # create EPUB file
    epub.write_epub(output_file, book)


def main():
    print('------------------ Generating now --------------------------------')

    title= 'Player who returned 10000 years later'

    book = epub.EpubBook()
    book.set_identifier('c32b599b-5e68-48a6-a852-e9ba8704367b')
    book.set_title(title)
    book.set_language('en')

    book.add_author('Butterfly Valley')
    book.set_cover("image.jpg", open('cover.jpg', 'rb').read())

    create_epub(book)

    print('eBook Created.')


if __name__ == '__main__' :
    main()
