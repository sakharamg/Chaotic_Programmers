var studentCompanionApp = angular.module('studentCompanionApp');



/**
 * Does routing of urls and controlelrs
 */
studentCompanionApp.config(function($stateProvider, $urlRouterProvider) {

    $urlRouterProvider.otherwise('/profile/home');

    $stateProvider

    // HOME STATES AND NESTED VIEWS ========================================

        .state('profile', {
        url: '/profile',
        templateUrl: 'views/profile.html',
        controller: 'profileCtrl',
    })

    .state('profile.home', {
        url: '/home',
        templateUrl: 'views/home.html',
        controller: 'indexCtrl',
    })

    .state('profile.friends', {
        url: '/friends',
        templateUrl: 'views/friends.html',
        controller: 'friendsCtrl',
    })

    .state('profile.leaderboard', {
        url: '/leaderboard',
        templateUrl: 'views/leaderboard.html',
        controller: 'leaderboardCtrl',
    })

    .state('profile.flashcards', {
        url: '/flashcards',
        templateUrl: 'views/flashcards.html',
        controller: 'flashcardCtrl',
    })

    .state('profile.flashcards.view', {
        url: '/view',
        templateUrl: 'views/flashcards_view.html'
    })

    .state('profile.flashcards.new', {
        url: '/new',
        templateUrl: 'views/flashcards_new.html'
    })

    .state('public', {
        url: '/public',
        templateUrl: 'views/login/index.html',
    })

    .state('public.login', {
        url: '/login',
        templateUrl: 'views/login/login_page.html',
        controller: 'loginCtrl',
    })

    .state('public.register', {
        url: '/register',
        templateUrl: 'views/login/register.html',
        controller: 'registerCtrl',
    })

    .state('profile.flashdecks', {
        url: '/flashdecks',
        templateUrl: 'views/flashdeck.html',
        controller: 'flashdeckCtrl',
    })


    .state('profile.flashdeck_show', {
        url: '/flashdeck_show?id',
        params: { 'id': null },
        templateUrl: 'views/flashdecks_show.html',
        controller: 'flashdeckShowCtrl',
    })

    .state('profile.flashcard_show', {
        url: '/flashcard_show?flashcard_id',
        params: { 'flashcard_id': null },
        templateUrl: 'views/flashcards_show.html',
        controller: 'flashcardShowCtrl',
    })


});