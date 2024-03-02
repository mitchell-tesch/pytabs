import pytabs


def main():
    # substantiate pyTABS EtabsModel
    etabs_model = pytabs.EtabsModel()

    stories = etabs_model.story.get_stories()
    
    print(stories)


if __name__ == "__main__":
    main()
